
# Visualisation of APR and Debt to Income ratio relation using D3.js

## Sergei Neviadomski

## Summary

In this project I used D3.js to visualize ralation between APR and Debt to Income ratio. I used open dataset that contains contains 113,937 loans with 81 variables on each loan from prosper.com. I calculated mean APR, mean Debt to Income ratio and Total Debt for every occupation in Python. After that I made a chart where every curcle represent occupation data. Y-axis shows average APR value. X-axis shows average Debt to Income ratio. Size of circle represent Size of Total Debt.      

## Design

At my first step I analysed row data in Python and came up with initial idea. I thought that it would be interesting to observe average APR rates for different occupations. Next idea was to add average Debt to Income ratio to my plot. At this point I had a scaterplot with interesting trend. Occupations with higher APR tend to have higher Debt ot Income ratio. After that I added Total debt to my polt. It is represented by size of circles. 

After getting feedback from my friend I added tooltips. So now you can get all the information about circle by hovering over it. I adjusted styling of my chart, so now it looks much better. I also added comments to mode and made it more readable.

## Feedback

I gathered feedback from 3 different people. Here I want to highlight 3 blocks of recomendations I got:

1. Visualisation:
    * Add tooltips to yor circles
* Styling:
    * Add Axes names
    * Adjust length of axis
    * Add X-axis ticks and change formating
    * Make styling of chart more beautiful and light
* Code:
    * Add comments to your code
    * Make your code more readable
    * Make indentation more consistent
    
I made a lot of chnges based of these feedbacks and now my chart looks much better.
