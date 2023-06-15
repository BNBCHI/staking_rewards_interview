def estimate_apr(staking_ratio_base, target_staking_ratio):
    """function to estimate APR"""
    # convert target_apr and apr_ratio_base to decimal
    target_staking_ratio = float(target_staking_ratio / 100)
    staking_ratio_base = float(staking_ratio_base/100)

    current_apr = 0.0567  # current APR from website
    current_staking_ratio = 0.1614  # current staking ratio from website

    # if current ratio is 0.0567 then estimated ratio should be cross multiplied
    apr_base = (staking_ratio_base * current_apr) / current_staking_ratio
    calc_apr = (target_staking_ratio * apr_base) / staking_ratio_base
    print(calc_apr)


estimate_apr(staking_ratio_base=15, target_staking_ratio=50)
