# EC-777 Problem Set 1

### Michaela Philip

## Model
**Specify the consumer’s (indirect) utility function. Define every parameter and variable in your utility function. If your function includes vectors of variables, please define each element of the vector.**

 We can write the consumer's indirect utility as 

$$
V_{ijt} = \alpha_i p_{ijt} + \beta_i' x_{jt} + \gamma_i' z_{it} +\xi_{jt} + \epsilon_{ijt}
$$

where $x_{jt}$ is a vector of observed variables containing the plan $j$'s actuarial value (AV), HMO status, and insurer at time $t$. The variable $p_{ijt}$ represents the plan's premium for household $i$, $\xi_{jt}$ represents unobserved characteristics, $z_{it}$ is a vector of demographic characteristics, and $\alpha$ and $\beta$ are our parameters.

**What is the outside option? What is the utility of the outside option?**

The outside option here is to not purchase insurance and incur a penalty. We can write this as 

$$
\tilde{V}_{i0t} = \rho_{it}
$$

where $\rho_{it}$ is the household penalty.

**Suppose policymakers are interested in how price sensitivity varies with age. Modify your utility function in 1(a) to allow price sensitivity to vary with age.**
    

$$
V_{ij} = \alpha_i p_{ijt} + \sum_{k\in K} \lambda_{ik} (a_{ik} \times p_{ijt}) + \sum_{k \in K} \delta_{ik} a_{ik} + \gamma_i' z_{it} + \beta_i' x_{jt} + \xi_{jt} + \epsilon_{ijt}
$$

where $a_{ik}$ is a dummy for age categories.

**What variation is there in the data that can identify the price parameter?**

The penalty was phased in from 2014-2016 which creates variation in price that we can exploit.

**Why might the premium be endogenous? What would be ideal instruments in this setting? Given the available data, what instruments can you construct?**
Premiums are endogenous because they are correlated with unobserved health risk.

**Your utility equations do not capture cost sharing subsidies, which have the effect of increasing the actuarial value of plans in the silver tier. For the lowest income exchange consumers the increase in AV is very substantial. How do you think the omission of cost sharing subsidies will bias your estimates of the premium and AV parameters?**


## Estimation

**Estimate the parameters of the utility function in 1(a) as a logit and nested logit using the inversion approach of Berry (1994).**

**Suppose that that the coefficients $\beta_{ik}$ of the product characteristics AV and HMO are normally distributed with mean $\bar{\beta_k}$ and variance $\sigma_k^2$. Estimate the utility and random coefficient parameters using the approach of BLP (1995). Compare your estimates to the logit and nested logit estimates in 2(a).**

**Use either the logit or nested logit to estimate the parameters of the utility function in 1(c). You can also try estimating separate models by age group. Discuss you results.**

**(Optional) Estimate the utility function as a logit at the household level using maximum likelihood. How do the estimated parameters compare to your estimates in 2(a)? (Note: there are packages in R or Stata to estimate a logit at the household level).**
## Results

**Compute the mean own-price elasticity of demand and mean cross-price elasticity of demand using the estimated parameters from each of the 3 models estimated in 2(a). How do the estimated elasticities vary across the 3 models?**

**Compute the mean own-price elasticity of demand and mean cross-price elasticity of demand by age group using the estimated parameters in 2(c). Do your estimated elasticities make sense?**

**Congress set the penalty for not having insurance to 0 starting in 2019. Compare enrollment before and after the policy change using your estimated model in 2(c). Discuss the effects on total enrollment in the insurance exchange, enrollment across the 4 metal tiers, enrollment by age group, and enrollment by firm. You can assume that insurers do not adjust premiums in response to the policy change.**