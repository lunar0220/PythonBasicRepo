// class MathHelper{
//     static PI = 3.14159265;

//     static squere(n){return n * n;}
//     static cube(n){return n * n * n}
//     static abs(n) {return n < 0 ? -n: n;}

//     static cicleArea(r){return MathHelper.PI * MathHelper.squere(r);}
//     static clamp(value, min, max){return Math.min(Math.max(value, min), max);}
// }


// console.log(MathHelper.squere(5));
// console.log(MathHelper.cube(3));
// console.log(MathHelper.cicleArea(7));
// console.log(MathHelper.clamp(150, 5, 100))





// class Color{
//     constructor(r, g, b){
//         this.r = r;
//         this.g = g;
//         this.b = b;
//     }
//     static fromHex(hex){
//         let r = parseInt(hex.slice(1, 3), 16 );
//         let g = parseInt(hex.slice(3, 5), 16 );
//         let b = parseInt(hex.slice(5, 7), 16 );

//         return new Color(r, g, b);
//     }

//     toString(){
//         return `rgb(${this.r}, ${this.g}, ${this.b})`;
//     }
// }

// let red = Color.fromHex('#FF0733');
// console.log(red.toString())



class Character{
    #health; //приватная штука позльзоваться внутри только
    constructor(name, maxHealth, attackPower){
        this.name = name;
        this.maxHealth = maxHealth;
        this.#health = maxHealth;
        this.attackPower = attackPower;
        this.level = 1;
        this.experience = 0;
    }

    get health(){return this.#health;}
    get isAlive(){return this.#health > 0;}

    takeDamege(amount){
        this.#health = Math.max(0, this.#health - amount);
    }

    heal(amount){
        this.#health = Math.min(this.maxHealth, this.#health + amount);
        console.log(`${this.name} восстановил ${amount} HP`);
    }

    attack(target){
        let damege = this.attackPower + Math.floor(Math.random() * 5);
        target.takeDamege(damege);
        console.log(`${this.name} атакует ${target.name} на  ${damege} урона!` +
        `(HP: ${target.health}/${target.maxHealth})`
        );
    }

    getStatus() {
        let bar = '🁢'.repeat(Math.floor(this.#health / this.maxHealth * 10));
        // bar += '🁣'.repeat(10 - bar.length);
        return `${this.name} [${bar}] ${this.#health}/${this.maxHealth} HP`;
    }
}

class Warrior extends Character {
    constructor(name) {
        super(name, 100, 15);
        this.shield = 10;
    }

    takeDamege(ammount){
        let reduced = Math.max(0, ammount - this.shield);
        super.takeDamege(reduced);
        console.log(`  Щит поглотил ${ammount - reduced} урона.`)  
    }

    shieldBash(target){
        console.log(`${this.name} использует удар щитом.`);
        target.takeDamege(this.attackPower * 1.5);
    }
}

class Mage extends Character{
    constructor(name){
        super(name, 70, 25);
        this.mana = 100;
    }

    castFireball(target){
        if(this.mana < 30){
            console.log(`${this.name}: НЕ ДОСТОЧНО МАНЫ!!!!`);
            return;
        }
        this.mana -= 30;
        let damege = 40 + Math.floor(Math.random() * 20);
        target.takeDamege(damege);
        console.log(`${this.name} кастует огенный шар! Урон: ${damege}` +
            `(Мана% ${this.mana}/100)`
        )
    }
}


let hero = new Warrior('Аанг');
let boss = new Mage('Зуко');

console.log("🥳Начало боя");
console.log('='.repeat(40));

let round = 1;
while(hero.isAlive && boss.isAlive){
    console.log(`\n---- Раунд ${round} -----`)
    
    console.log(hero.getStatus());
    console.log(boss.getStatus());

    hero.attack(boss);
    if(boss.isAlive){
        if(round % 3 === 0){
            boss.castFireball(hero);
        } else{
            boss.attack(hero);
        }
    }

    round++;

    if(round > 20) break;
}

console.log('\n' + '='.repeat(40));
if(hero.isAlive){
    console.log(`${hero.name} победил!!!!`)
} else {
    console.log(`${boss.name} победил!!!!`)
}