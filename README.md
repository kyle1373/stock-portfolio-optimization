# Portfolio Optimization with Machine Learning

[embed]https://kylewade.dev/stock_portfolio_optimization.pdf[/embed]

> Yalu Ouyang, Darell Chua, Dirk Xie, Kyle Wade


In our project, we set out to tackle the problem of portfolio optimization - changing the weighting consituent stocks for maximum return on investment - through the application of machine learning techniques.

To do so, we've compiled stock prices of dozens of publicly listed companies over the period 2014-2024, and performed experiments with stock portfolios constructed from this dataset.

Our methodology breaks down to 3 different approaches:

- MVO (mean-variance optimization) and MVO-based Neural Networks
- Neural Network with separate optimizer
- Neural Network with embedded optimizer

## MVO and MVO-based Neural Networks

![MVO](sample_results/MVO.png)

![MVO with risk aversion factor](sample_results/MVO%20with%20Risk.png)

![MVO-based Neural Network](sample_results/Optimal%20MVO%20and%20NN%20portfolio.png)

## Neural Network with separate optimizer

![NN with separate optimizaer](sample_results/NN_with_separate_optim.png)


## Neural Network with embedded optimizer

<img width="945" alt="image" src="https://github.com/kyle1373/ece228-project/assets/59634395/54f4f2fb-5ee6-4e27-8d02-ca1a9c91d52a">
