#!/bin/usr/env python
# Formelsamlung Wahrscheinlichkeiten

import pandas as pd
import numpy as np 
import networkx as nx

def factorial(n):
    """Factorial of n."""

    assert isinstance(n, int)
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

def nchoosek(n, k):
    """Binominal Coefficient choose k from n."""

    assert isinstance(n, int)
    assert isinstance(k, int)
    assert n>=k

    return int(factorial(n) / factorial(k) / factorial(n-k))


def laplace_probability(n, k, p):
    """Laplace Probability of k events from n with probability p."""

    assert isinstance(n, int)
    assert isinstance(k, int)
    assert n>=k
    assert isinstance(p, float)
    assert p>=0 and p<=1

    return nchoosek(n, k) * p**k * (1-p)**(n-k)


def unconditional_truth_table(probability_a, probability_b,
                              label_a='A', label_b='B'):
    """Print a truth table from p(a) and p(b)."""

    columns=[label_a, '¬' + label_a, 'sum']
    index=[label_b, '¬' + label_b, 'sum']

    prob_ab = probability_a * probability_b
    prob_notab =  (1-probability_a) * probability_b
    prob_anotb = probability_a * (1-probability_b)
    prob_notanotb = (1-probability_a) * (1-probability_b)

    prob_a = prob_ab + prob_anotb
    prob_nota = prob_notab + prob_notanotb
    prob_b = prob_ab + prob_notab
    prob_notb = prob_anotb + prob_notanotb
    check = float(np.isclose(prob_a + prob_nota, 1) and
                  np.isclose(prob_b + prob_notb, 1))

    data = np.array([[prob_ab, prob_notab, prob_b],
                     [prob_anotb, prob_notanotb, prob_notb],
                     [prob_a, prob_nota, check]])
                     
    df = pd.DataFrame(data=data, index=index, columns=columns)

    columns=['Probability']
    index=['p( %s)' % (label_a),
           'p(¬%s)' % (label_a),
           'p( %s)' % (label_b),
           'p(¬%s)' % (label_b),
           'p( %s ∩  %s)' % (label_a, label_b),
           'p( %s ∩ ¬%s)' % (label_a, label_b),
           'p(¬%s ∩  %s)' % (label_a, label_b),
           'p(¬%s ∩ ¬%s)' % (label_a, label_b),
           'p( %s |  %s)' % (label_a, label_b),
           'p(¬%s |  %s)' % (label_a, label_b),
           'p( %s |  %s)' % (label_a, label_b),
           'p(¬%s | ¬%s)' % (label_a, label_b)]

    data = np.array([prob_a,
                     prob_nota,
                     prob_b,
                     prob_notb,
                     prob_ab, 
                     prob_anotb,
                     prob_notab,
                     prob_notanotb,
                     prob_ab / prob_b, 
                     prob_notab / prob_b,
                     prob_anotb / prob_notb,
                     prob_notanotb / prob_notb])

    summary = pd.DataFrame(data=data, index=index, columns=columns)

    G = nx.Graph()
    G.add_edges_from(
        [('A', 'B'), ('A', '¬B')]
    )
    nx.draw(G)

    return df, summary