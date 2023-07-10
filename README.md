# arbitrbot

During the course "Financial Markets" at the Higher School of Economics (HSE), we were introduced to the trading strategy called pair arbitrage. In a nutshell, pair arbitrage involves two or more assets in the market that have high correlation in their price movements due to various factors such as belonging to the same industry or issuer.

This leads to the formation of a stable average spread, which is the price difference between Asset A and Asset B. If the price of Asset A sharply increases while the price of Asset B remains at the same level, it can be reasonably assumed that the price of Asset B will also start to rise in order to bring the current spread between these assets back to its average value.

Therefore (more details in the file "Algorithm.md"), trades can be executed in such a way that the direction of the price movement of the assets becomes irrelevant. The only factor of interest would be the spread between them. To test this theory, we decided to develop an algorithm that would automatically execute trades based on this strategy.
