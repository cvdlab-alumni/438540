/* write a script containing the function fibonacci(i)
that returns the i-th element of the Fibonacci's serie (apply memoization pattern) */

function fibonacci (n) {
  if (!(n in fibonacci)) {
  	fibonacci[n] = fibonacci(n-1) + fibonacci(n-2);
  }
  return fibonacci[n];
}

// Initialize the cache to hold this base case.
fibonacci[1] = 1;  
fibonacci[2] = 1;
