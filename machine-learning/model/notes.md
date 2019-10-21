# **Linear Regression**

### `a = wx + b`

* `a` is predicted value
* `w` is weight
* `x` is variable
* `b` is bias

# **Multiple Linear Regression**

### `a = w1x1 + w2x2 + w3x3 + b`

* `a` is predicted value
* `w` is weight
* `x` is variable
* `b` is bias


# **Graham Forumula**

```
Graham Formula = (EPS * (8.5 + 2g) * 4.4) / Y

V = the value expected from the growth formulas over the next 7 to 10 years
EPS= the company’s last 12-month earnings per share
8.5 = P/E base for a no-growth company
g = reasonably expected 7 to 10 year growth rate (see Sustainable growth rate #From a financial perspective)
4.4 = the average yield of AAA corporate bonds in 1962 (Graham did not specify the duration of the bonds, though it has been asserted that he used 20 year AAA bonds as his benchmark for this variable[4])
Y= the current yield on AAA corporate bonds.
```
We want to idealize the values of `P/E` and `g`.
* `V = (EPS * (y + ug) * 4.4) / Y`
* `V = ((4.4 * EPS) / Y) * (y + ug)`

    let `Z = ((4.4 * EPS) / Y)`
* `V = Z(y + ug)`
* `V = Zy + Zug`

    let `Q = Z * g`
* `V = Zy + Qu`

In a linear model, the following can be interpreted.
* `V = a`, 
* `Z = x1`,
* `Q = x2`,
* `y = w1`, 
* `u = w2`, 

So, `V = Zy + Qu` becomes `a = w1x1 + w2x2` .

For linear regression, `V = Zy + Qu + b` .

-------------------------------------
-------------------------------------
-------------------------------------
# *Notes*
First step, begin showing data. Establish data that it is being trained on (y, u, V). Will likely need to normalize features (`23:26`)

Then, create model. `(05:37)`
