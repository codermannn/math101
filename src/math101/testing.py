"""
Self-testing and retrieval practice utilities.

These tools implement the Testing Effect — the most powerful learning
technique identified in cognitive science. They force active recall
rather than passive re-reading.
"""

import numpy as np
import sys


# ANSI color codes for terminal output
_GREEN = '\033[92m'
_RED = '\033[91m'
_YELLOW = '\033[93m'
_CYAN = '\033[96m'
_BOLD = '\033[1m'
_RESET = '\033[0m'


def check_answer(student_answer, correct_answer, question="", hint="", tolerance=None):
    """Check a student's answer against the correct answer.
    
    Parameters
    ----------
    student_answer : any
        The student's answer.
    correct_answer : any
        The correct answer.
    question : str
        The question being answered (for display).
    hint : str
        Hint to show if wrong.
    tolerance : float or None
        For numeric answers, accept if within this tolerance.
    
    Returns
    -------
    correct : bool
    """
    if question:
        print(f"{_CYAN}Q: {question}{_RESET}")
    
    if tolerance is not None and isinstance(student_answer, (int, float)):
        correct = abs(student_answer - correct_answer) <= tolerance
    elif isinstance(correct_answer, np.ndarray):
        correct = np.allclose(student_answer, correct_answer)
    else:
        correct = student_answer == correct_answer
    
    if correct:
        print(f"{_GREEN}{_BOLD}✅ Correct!{_RESET} Answer: {correct_answer}")
    else:
        print(f"{_RED}{_BOLD}❌ Not quite.{_RESET} Your answer: {student_answer}")
        if hint:
            print(f"{_YELLOW}💡 Hint: {hint}{_RESET}")
        else:
            print(f"   Expected: {correct_answer}")
    
    return correct


def check_complexity(student_answer, correct_answer, question=""):
    """Check a Big-O complexity answer.
    
    Accepts common variations: 'O(n)', 'n', 'O(n log n)', 'n log n', etc.
    
    Parameters
    ----------
    student_answer : str
        Student's complexity answer, e.g., 'O(n log n)' or 'n^2'.
    correct_answer : str
        Correct complexity, e.g., 'O(n log n)'.
    question : str
        The question being answered.
    """
    # Normalize both answers
    def normalize(s):
        s = s.strip().lower()
        s = s.replace('o(', '').replace(')', '')
        s = s.replace('^', '**')
        s = s.replace('²', '**2')
        s = s.replace('³', '**3')
        s = s.replace('ⁿ', '**n')
        s = s.replace(' ', '')
        s = s.replace('logn', 'log n').replace('log(n)', 'log n')
        return s
    
    return check_answer(
        normalize(student_answer),
        normalize(correct_answer),
        question=question,
        hint=f"The correct complexity is {correct_answer}"
    )


def predict_then_run(description, prediction_prompt, actual_func, 
                     student_prediction=None):
    """Predict-then-verify exercise pattern.
    
    This implements the most effective form of retrieval practice:
    force a prediction, then immediately show the truth.
    
    Parameters
    ----------
    description : str
        What we're about to compute.
    prediction_prompt : str
        Question to ask the student.
    actual_func : callable
        Function that computes and returns the actual answer.
    student_prediction : any
        Student's prediction. If None, just shows the result.
    
    Returns
    -------
    actual : any
        The actual computed result.
    """
    print(f"{_BOLD}📋 {description}{_RESET}")
    print(f"{_CYAN}🤔 Predict: {prediction_prompt}{_RESET}")
    
    actual = actual_func()
    
    if student_prediction is not None:
        print(f"   Your prediction: {student_prediction}")
        print(f"   Actual result:   {actual}")
        if student_prediction == actual:
            print(f"{_GREEN}✅ Your intuition is strong!{_RESET}")
        else:
            print(f"{_YELLOW}📖 Review this concept — the gap between prediction and reality is where learning happens.{_RESET}")
    else:
        print(f"   Result: {actual}")
        print(f"{_YELLOW}(Fill in student_prediction to test yourself!){_RESET}")
    
    return actual


def difficulty_banner(level):
    """Print a difficulty level banner.
    
    Parameters
    ----------
    level : str
        One of 'warmup', 'challenge', 'boss'.
    """
    banners = {
        'warmup': f"\n{_GREEN}{'='*60}\n🟢 WARM-UP: Predict the output, then run to verify\n{'='*60}{_RESET}\n",
        'challenge': f"\n{_YELLOW}{'='*60}\n🟡 CHALLENGE: Modify the code to handle a new constraint\n{'='*60}{_RESET}\n",
        'boss': f"\n{_RED}{'='*60}\n🔴 BOSS LEVEL: Implement from scratch without reference\n{'='*60}{_RESET}\n",
    }
    print(banners.get(level, f"\n{level}\n"))


def score_report(results):
    """Print a summary score from a list of True/False check results.
    
    Parameters
    ----------
    results : list of bool
        Results from check_answer calls.
    """
    total = len(results)
    correct = sum(results)
    pct = (correct / total * 100) if total > 0 else 0
    
    print(f"\n{_BOLD}{'='*40}")
    print(f"📊 SCORE: {correct}/{total} ({pct:.0f}%)")
    print(f"{'='*40}{_RESET}")
    
    if pct == 100:
        print(f"{_GREEN}🏆 Perfect! You've mastered this section.{_RESET}")
    elif pct >= 80:
        print(f"{_GREEN}💪 Strong understanding. Review the ones you missed.{_RESET}")
    elif pct >= 60:
        print(f"{_YELLOW}📖 Decent, but re-read the concepts and try again.{_RESET}")
    else:
        print(f"{_RED}🔄 Go back to the main notebook and study the examples, then retry.{_RESET}")
