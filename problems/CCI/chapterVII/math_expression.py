"""
Suppose you were asked to write a function to add two simple mathematical expressions which are of the form Ax• + Bxb + . . . (where the coefficients and exponents can be any positive or negative real number). That is, the expression is a sequence of terms, where each term is simply a constant times an exponent. The interviewer also adds that she doesn't want you to have to do string parsing, so you can use whatever data structure you'd like to hold the expressions.
"""

from typing import Optional
from dataclasses import dataclass, field, replace


@dataclass
class Term:
    coefficient: int
    exponent: int
    next: Optional["Term"] = None


@dataclass
class Expression:
    head: Optional[Term] = None

    
def add_expr(expr_a: Expression, expr_b: Expression) -> Expression:
    head = Term(0, 0)
    runner = head
    term_a = expr_a.head
    term_b = expr_b.head
    while term_b and term_a:
        if term_a.exponent < term_b.exponent:
            runner.next = replace(term_a)
            runner = runner.next
            term_a = term_a.next
        elif term_a.exponent > term_b.exponent:
            runner.next = replace(term_b)
            runner = runner.next
            term_b = term_b.next
        else:
            sum_term = add_term(term_a, term_b)
            runner.next = replace(sum_term)
            runner = runner.next
            term_a = term_a.next
            term_b = term_b.next
    term = term_a or term_b
    while term:
        runner.next = replace(term)
        runner = runner.next
        term = term.next
    return Expression(head.next)


def add_term(term_a: Term, term_b: Term) -> Term:
    return Term(term_a.coefficient + term_b.coefficient, term_a.exponent)

            
def test_add():
    expr_a = Expression(Term(1, 1, Term(1, 2)))
    expr_b = Expression(Term(1, 1, Term(1, 3)))
    expected = Expression(Term(2, 1, Term(1, 2, Term(1, 3))))
    assert compare_expr(add_expr(expr_a, expr_b), expected)


def compare_expr(expr_a: Expression, expr_b: Expression) -> bool:
    return expr_a == expr_b


def compare_term(term_a: Term, term_b: Term) -> bool:
    return term_a == term_b

    
test_add()
