
# Visualisation of APR and Debt to Income ratio relation using D3.js

## Sergei Neviadomski

## Summary

In this project I used D3.js to visualize APR and Debt to Income ratio among different occupations. I used open dataset that contains contains 113,937 loans with 81 variables on each loan from prosper.com. I calculated mean APR, mean Debt to Income ratio and Total Debt for every occupation in Python.  

At my first step I analysed row data in Python and came up with initial idea. I thought that it would be interesting to observe average APR rates for different occupations. Next idea was to add average Debt to Income ratio to my plot. At this point I had a scaterplot with interesting trend. Occupations with higher APR tend to have higher Debt ot Income ratio. After that I added Total debt to my polt. It is represented by size of circles. 

## Design

On my chart every bubble represents one occupation. Different colors shows different occupations. This data is not very important, just helps find occupation you are looking for. APR and Debt to Income ratio is much more important. I decided to show this data by positioning of bubbles along Y and X axes respectively. Size of the bubble is a Total Debt for this occupation.  

After getting feedback from my friends I analysed and devided them into next 3 categories:

1. Visualisation:
    * Add tooltips to yor bubbles
    * Add legend
* Styling:
    * Add Axes names
    * Adjust length of axis
    * Add X-axis ticks and change formating
    * Make styling of chart more beautiful and light
* Code:
    * Add comments to your code
    * Make your code more readable
    * Make indentation more consistent
    
After that I added tooltips and legend. So now you can get all the information about circle by hovering over it or by hovering over occupation name in legend. I adjusted styling of my chart, so now it looks much better. I also added comments to code and made it more readable.

## Feedback

I gathered feedback from 4 different people. 

### Feedback 1

The main complaint of my first reviewer was that my chart is not beautiful and tick on X-axis marked is strange way. He also said that my code had inconsistent indentation. 

After getting my first feedback I adjusted length of my axes, added ticks on X-axis and changed format of ticks. I also corrected indentation of my code.

### Feedback 2

My second reviewer told me that I should add tooltips to my chart, because it's difficult to distinguish between occupations.

That was a good advice. I inplemented this in my next version of chart. 

### Feedback 3

My third reviewer said that I should add axes titles and comments to my code.

I agreed and did all he said.

### Feedback 4

The main complaint of my fourth reviewer was that it's still difficult to find occupation that somebody is looking for. He said that it's a good idea to add legend to my chart.

I added the legend. Now you can hover over occupation in legend and appropriate bubble will be highlighted.
