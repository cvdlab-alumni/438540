/* exercise01a
write a function that pushes into an array the first n natural numbers */
var array =[]
function natural(n) {
	var a=[];
	var i;
	for(i=1; i<=n; i++){
		a.push(i);
	}
	return a;
}

/* exercise01b
filter out odd number and return the even ones */
function pari(array) {
	return array.filter(function (item) { 
		return item%2 === 0; 
	})
}

/* exercise01c
double each even number obtained */
function raddoppia(array) {
	return array.map(function (item) {
		return item * 2;
	})
}

/* exercise01d
return only numbers divisible by 4 */
function divisibili(array) {
	return array.filter(function (item) { 
		return item%4 === 0; 
	})
}

/* exercise01e
sum all the remaining numbers */
function somma(array) {
	return array.reduce(function (prev,cur) { 
		return prev + cur; 
	})
}

array = natural(50);
array = pari(array);
array = raddoppia(array);
array = divisibili(array);
array = somma(array);