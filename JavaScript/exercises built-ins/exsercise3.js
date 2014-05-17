/* exercise03a
write a function that given a word return it capitalized */
function capitalizedWord(word) {
	var c = (word.charAt()).toUpperCase();
	var rest = word.slice(1,word.lenght);
	return c+rest;

}

/* exercise03b
write a function that capitalize each word of the following text: 
"Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." */

// perche' non va?
function capitalizedText(text) {
	var i; 
	var s = [];
	var c;
	console.log(s);
	for (i=0; i<text.lenght; ++i) {
		c = text[i];
		if (c===" ") {
			c = c.toUpperCase();
		}
		s.push(c);
	}
	return s;
}


function Rectangle (x, y, width, height) {
  Shape.call(this, x, y); // call "super" constructor
  this.width = width;
  this.height = height;
  this.prototype = Object.create(Shape.prototype);
  this.prototype.constructor = this;
}




