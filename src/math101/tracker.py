"""
Study tracker for spaced repetition.

Logs completion dates and suggests when to review each module
based on expanding intervals (1, 3, 7, 14, 30 days).
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path


_TRACKER_FILE = Path(__file__).parent.parent.parent.parent / "DSA_MATH_INTUITION" / ".study_progress.json"

# Spaced repetition intervals in days
_REVIEW_INTERVALS = [1, 3, 7, 14, 30]


def _load_progress():
    """Load progress from disk."""
    if _TRACKER_FILE.exists():
        with open(_TRACKER_FILE, 'r') as f:
            return json.load(f)
    return {"modules": {}, "exercises": {}}


def _save_progress(data):
    """Save progress to disk."""
    _TRACKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(_TRACKER_FILE, 'w') as f:
        json.dump(data, f, indent=2, default=str)


def mark_complete(module_name, notebook_name=None):
    """Mark a module or notebook as completed today.
    
    Parameters
    ----------
    module_name : str
        e.g., 'Growth_and_Complexity'
    notebook_name : str or None
        e.g., '01_unified_growth_explorer'
    """
    data = _load_progress()
    now = datetime.now().isoformat()
    
    if module_name not in data["modules"]:
        data["modules"][module_name] = {
            "first_completed": now,
            "last_reviewed": now,
            "review_count": 0,
            "notebooks": {}
        }
    
    module = data["modules"][module_name]
    module["last_reviewed"] = now
    module["review_count"] = module.get("review_count", 0) + 1
    
    if notebook_name:
        module["notebooks"][notebook_name] = {
            "completed": now,
            "score": None
        }
    
    _save_progress(data)
    print(f"✅ Marked '{module_name}' as reviewed on {datetime.now().strftime('%Y-%m-%d')}")


def record_score(module_name, notebook_name, score, total):
    """Record an exercise score.
    
    Parameters
    ----------
    module_name : str
    notebook_name : str
    score : int
        Number correct.
    total : int
        Total questions.
    """
    data = _load_progress()
    now = datetime.now().isoformat()
    
    if "exercises" not in data:
        data["exercises"] = {}
    
    key = f"{module_name}/{notebook_name}"
    if key not in data["exercises"]:
        data["exercises"][key] = []
    
    data["exercises"][key].append({
        "date": now,
        "score": score,
        "total": total,
        "percentage": round(score / total * 100, 1)
    })
    
    _save_progress(data)
    print(f"📊 Score recorded: {score}/{total} ({score/total*100:.0f}%)")


def review_schedule():
    """Print what's due for review based on spaced repetition intervals.
    
    Returns
    -------
    due : list of str
        Module names due for review.
    """
    data = _load_progress()
    now = datetime.now()
    due = []
    upcoming = []
    
    print("\n📅 STUDY REVIEW SCHEDULE")
    print("=" * 50)
    
    if not data["modules"]:
        print("No modules completed yet. Start with TOOLS_PRIMER/!")
        return []
    
    for name, info in data["modules"].items():
        last = datetime.fromisoformat(info["last_reviewed"])
        review_count = info.get("review_count", 0)
        
        # Determine next review interval
        interval_idx = min(review_count, len(_REVIEW_INTERVALS) - 1)
        interval = _REVIEW_INTERVALS[interval_idx]
        next_review = last + timedelta(days=interval)
        
        days_until = (next_review - now).days
        
        if days_until <= 0:
            due.append(name)
            print(f"  🔴 {name} — DUE NOW (last reviewed {(now - last).days} days ago)")
        elif days_until <= 2:
            upcoming.append(name)
            print(f"  🟡 {name} — due in {days_until} day(s)")
        else:
            print(f"  🟢 {name} — next review in {days_until} days")
    
    if due:
        print(f"\n⚡ {len(due)} module(s) due for review!")
    else:
        print(f"\n✅ All caught up! Next review coming soon.")
    
    # Show exercise history
    if data.get("exercises"):
        print(f"\n📊 EXERCISE HISTORY")
        print("-" * 50)
        for key, attempts in data["exercises"].items():
            latest = attempts[-1]
            trend = ""
            if len(attempts) > 1:
                prev = attempts[-2]["percentage"]
                curr = latest["percentage"]
                trend = " 📈" if curr > prev else (" 📉" if curr < prev else " ➡️")
            print(f"  {key}: {latest['percentage']}%{trend} ({len(attempts)} attempt(s))")
    
    return due


def reset_progress():
    """Reset all progress data."""
    if _TRACKER_FILE.exists():
        os.remove(_TRACKER_FILE)
    print("🔄 Progress reset.")
