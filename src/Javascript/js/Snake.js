class Snake {
	constructor(ctx) {
		this.body = [[0, 0]];
		this.ctx = ctx;
	}

	addBody() {
		this.body.push(this.body[this.body.length - 1].map((pos, index) => pos - speed[index]));
	}

	hasCollidedWithFruit() {
		return this.body[0][0] == fruit.position[0] && this.body[0][1] == fruit.position[1];
	}

	hasCollidedWithItself() {
		return this.body.slice(1).some(pos => pos[0] == this.body[0][0] && pos[1] == this.body[0][1])
	}

	hasReachedMaximumBody() {
		return this.body.length == (GRID[0] - 1) ** 2;
	}

	calculateNextPosition() {
		return this.body[0].map((pos, index) => pos + speed[index]);
	}

	draw() {
		this.ctx.fillStyle = 'green';
			
		for (const position of this.body)
			ctx.fillRect(...position.map(pos => pos * PIXEL_OFFSET), PIXEL_OFFSET, PIXEL_OFFSET);
	}

	update() {
		// Update position
		let [x, y] = this.calculateNextPosition();
				
		if (x * PIXEL_OFFSET >= canvas.width) {
			x = 0;
		}
				
		if (x * PIXEL_OFFSET <= -PIXEL_OFFSET) {
			x = GRID[0];
		}
		
		if (y * PIXEL_OFFSET >= canvas.height) {
			y = 0;
		}
		
		if (y * PIXEL_OFFSET <= -PIXEL_OFFSET) {
			y = GRID[1];
		}
		
		this.body.pop();
		this.body.unshift([x, y]);

		// Has Collided with Fruit
		if (this.hasCollidedWithFruit())
			this.eat();

		// Update Game Status
		if (this.hasCollidedWithItself()) {
			status = 'lose';
		} else if (this.hasReachedMaximumBody()) {
			status = 'win';
		}
	}

	eat() {
		this.addBody();
		fruit.spawn();
	}
}