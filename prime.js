#!/usr/bin/env node

console.log("begin");  
primes = [2];
n = 3;
p = 0;
console.log("begin");
	while (primes.length < 20000) {
		p = 0;
		primes.push(n);
		n = n + 2;
		while (p <= primes.length) {
			if (n%primes[p] == 0) {  
				p = 0;
				n = n +2;
				} 
			else p = p +1;
				
    				};

};
prime = String(primes);

console.log(prime);

