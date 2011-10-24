var vending = require("./vending.js");

exports["Test Passa N e CoinReturn e recebe um N"] = function(test) {
    var result = vending.vend("N", "COIN-RETURN");
    test.equal(result, "N");
    test.done();
}

exports["Test Passa D e CoinReturn e recebe um D"] = function(test) {
    var result = vending.vend("D", "COIN-RETURN");
    test.equal(result, "D");
    test.done();
}

exports["Test Passa Q e CoinReturn e recebe um Q"] = function(test) {
    var result = vending.vend("Q", "COIN-RETURN");
    test.equal(result, "Q");
    test.done();
}
exports["Test Passa DOLLAR e CoinReturn e recebe um DOLLAR"] = function(test) {
    var result = vending.vend("DOLLAR", "COIN-RETURN");
    test.equal(result, "DOLLAR");
    test.done();
}

exports["Test Passa N e D e CoinReturn e recebe N e D"] = function(test) {
    var result = vending.vend("N,D", "COIN-RETURN");
    test.strictEqual(result, "N,D");
    test.done();
}

exports["Test Passa 2QDN e GET-A e recebe A"] = function(test) {
    var result = vending.vend("Q,Q,D,N", "GET-A");
    test.strictEqual(result, "A");
    test.done();
}

exports["Test Passa DOLLAR e GET-B e recebe B"] = function(test) {
    var result = vending.vend("DOLLAR", "GET-B");
    test.strictEqual(result, "B");
    test.done();
}

exports["Test Passa DOLLARQQ e GET-C e recebe C"] = function(test) {
    var result = vending.vend("DOLLAR,Q,Q", "GET-C");
    test.strictEqual(result, "C");
    test.done();
}

exports["Converte"] = function(test) {
    var result = vending.convert(0.15);
    test.strictEqual(result, "D,N");
    test.done();
}

/*exports["Test Passa DOLLAR e GET-A e recebe A e recebe QD"] = function(test) {
    var result = vending.vend("DOLLAR", "GET-A");
    test.strictEqual(result, "A,Q,D");
    test.done();
}

exports["Test Passa 3Q e GET-A e recebe A e recebe AD"] = function(test) {
    var result = vending.vend("Q,Q,Q", "GET-A");
    test.strictEqual(result, "A,D");
    test.done();
}*/