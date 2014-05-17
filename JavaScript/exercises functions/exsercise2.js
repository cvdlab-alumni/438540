/* write a script containing the function identity(n)
that returns the n rows by n columns identity matrix */


function identity(n) {
	var matrix = [];
	var i;
	var j;
	for (i=1; i<=n; i++){
		var row = [];
		for (j=1; j<=n; j++) {
			i===j ? row.push(1) : row.push(0);
		}
		matrix.push(row)
	}
	return matrix
};

