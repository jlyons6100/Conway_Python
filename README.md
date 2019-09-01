# Conway_Python

Game of life with a toroidal array using tkinter in python3.

### Version 1:
Simple Conway's Game of Life. 2D Matrix of 1's and 0's representing life. I iterate through the 2D array and draw squares on a Tkinter canvas. Relatively slow with larger matrix sizes.

### Versopn 2:
I used cProfile to see why program was slowing down. I was spending about half my time redrawing the board and the other half of the time generating the next generation. I thought about how I could improve that speed. As far as the board goes, I kept a list of positions that had changed since the last generation and only evaluated those. This lead to a huge boost in performance. A 650 x 650 array with 75% life initially went from taking ~7 seconds to calculate the next generation to under 1 second. Took similar steps and only redrew squares that had been changed on the canvas. However, I ran into a bottleneck. Even though cProfile shows my code runs in less than a second, it takes longer than that for the Tkinter canvas to update. Looking into ways to improve performance more in the future.

### Images:

![Image 1](https://github.com/jlyons6100/Conway_Python/blob/master/Images/image1.png)
![Image 2](https://github.com/jlyons6100/Conway_Python/blob/master/Images/image2.png)
