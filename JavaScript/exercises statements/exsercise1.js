var i;
var j;
var s;

for (i=1; i<=10; i +=1) {
	s += "\n";
	for (j=1; j<11; j+=1){
		s += i*j + "\t";
	}
}
console.log(s);