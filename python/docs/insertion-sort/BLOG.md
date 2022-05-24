# Insertion sorting blog

- Let's look at some pseudo code to get oriented with the logic:

- [Pseudo Code](pseudo-code.png)

- The first run through of our list is already sorted, so the first element in the list is right where is should be. Great! Let's move on:

- [First Photo](first-loop.png)

- Select the next element and compare it to the previous sorted element, meaning the first element in the list:

- [Second Photo](second-photo.png)

- We will repeat this in the next two iterations because both values are greater than the previous index:

- [Third Photo](third-photo.png)
- [Fourth Photo](fourth-photo.png)

- Now this iteration through the list we will want, the value of 16 is less than 42, and 23 so we will subtract from the index and compare down the list until it is greater than the index before it:

- [Fifth Photo](fifth-photo.png)

- We will repeat this with the value of 15, moving through the loop 3 times until it finds it's correct index:

- [Sixth Photo](sixth-photo.png)

- And there we have it folks! An insert method that will arrange the values of a list in ascending order.

- This method uses Big(O) of (N) because the space doesn't change at all and Big(O) of (1) because the time depends on how long the list is.
