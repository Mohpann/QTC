Some scripts written in python for the Quantitative Trading Club at UIC. 

The Epsilon Greedy Trading Algorithm was written in tandem with a now full-time equity and derivaties strategist at Wells Fargo. In order to see some information about a "dark pool", you need to send a buy/sell order to one.
Given a stock, we want to find a pool with the lowest bid price and buy in using that one. So we will send very small buy trades to many pools to assess which pool has the best bid price. Implementation shortfall is also considered.
In summary, this algorithm probes several different "dark pools" to find the best bid price to buy in at for a given stock. 
