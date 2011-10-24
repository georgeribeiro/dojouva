var valores = {"N":0.05, "D":0.1, "Q":0.25, "DOLLAR": 1.0};
var produtos = {"A":0.65, "B":1.0, "C":1.5};

function convert (val)  {
    var result = "";
    var v = val;
    while (v > 0.0)  {
        if (v >= 1.0)  {
          v -= 1.0;
          result += "DOLLAR,";
        }
        else if (v >= 0.25)  {
            v -= 0.25;
            result += "Q,";
        }
        else if (v >= 0.1)  {
            v -= 0.1;
            result += "D,";
        } 
        else if (v >= 0.05)  {
            v -= 0.05;
            result += "N,";
        }
    }
    var r = '';
    for (var i = 0; i < result.length - 1; i++) {
        r += result[i];
    };
    return r;
}

exports.convert = convert;

exports.vend = function(coins, command)
{
    var aux = 0.0;

    if(command == "COIN-RETURN")
    {
        return coins;
    }
    else
    {
        var lista_valores = coins.split(",");

        for (i in lista_valores)
        {
            aux += valores[lista_valores[i]];
        }

        if (aux >= produtos["A"] && command == 'GET-A')
        {
            if(aux == produtos["A"]){
            
                return "A";
            }
            else
            {
                troco = aux - produtos["A"];
                return "A,"+convert(troco);

            }
        } 
        else if (aux == produtos["B"] && command == 'GET-B') {
            return 'B';
        }
        else if(aux == produtos["C"] && command == 'GET-C') {
            return 'C';
        }

    }


    return coins;
}

