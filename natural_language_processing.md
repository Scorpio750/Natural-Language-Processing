# Natural Language Processing
## Matthew Stone
## 1/21/15

---
---

## 1/20/15

## Supervised Categorization

- Infer 
- Start from examples
- Learn decision boundary
- **Token detection**
- Apply learned rule to new cases

## Classification via Probability

- Item drawn from underlying category
- Represented as RV $$$C$$$
- Takes on values $$$\\{c_1, c_2,\dotsc,c_k\\}$$$
- Have *prior* probabilities $$$P(C = c_i)$$$
- We get a *feature vector* describing observation
- Represented as observation variable $$$O$$$
- Thus we get *likelihood*probability $$$P(O = o \mid C = c)$$$

## Generalization in Probabilistic Models

Key idea: independence assumptions

- Ignore certain kinds of interactions in the world
- Lets you use same data to learn multiple relationships
- Thus, cannot represent everything in the world

### Naive Bayes assumption

Each feature is independent of the others given the class

- Mathematically:

$$P(F_i\mid C) = P(F_i\mid C, F_1,\dotsc F\_{i-1})$$

- As a result:

$$P(F_1\dotso F_n\mid C) = P(F_1\mid C)\;P(F_2\mid C)\dotso P(F_n\mid C)$$


The hardest thing to know about machine learning is whether it's working