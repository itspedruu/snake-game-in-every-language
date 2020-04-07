class Fruit {
	constructor(ctx) {
		this.position = [];
		this.ctx = ctx;

		this.spawn();
	}

	draw() {
		this.ctx.fillStyle = 'red';
		this.ctx.fillRect(...this.position.map(pos => pos * PIXEL_OFFSET), PIXEL_OFFSET, PIXEL_OFFSET);
	}

	spawn() {
		const possibleX = Array(GRID[0]).fill().map((_, index) => index + 1).filter(x => !snake.body.some(([snakeX]) => snakeX == x));
		const possibleY = Array(GRID[1]).fill().map((_, index) => index + 1).filter(y => !snake.body.some(([_, snakeY]) => snakeY == y));
				
		this.position = [possibleX, possibleY].map(arr => arr[Math.floor(Math.random() * arr.length)]);
	}
}