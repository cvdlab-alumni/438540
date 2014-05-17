/* exercise02a
write a function that pushes into an array n random integer numbers */
var array = [];
function randomArray(n) {
	var a = [];
	var i;
	for (i=1; i<=n; i++) {
		x = Math.floor(Math.random() * (100 + 1));
		a.push(x)
	}
	return a;
};

/* exercise02b
filter even numbers and return the odd ones */
function dispari(array) {
	return array.filter(function (item) { 
		return item%2 !== 0; 
	})
};

/* exercise02c
sort obtained numbers from the smallest to the largest */

function crescente(array) {
	return array.sort(function (value1, value2) {
 return value1 - value2;
})
};

array = randomArray(50);
array = dispari(array);
array = crescente(array);
