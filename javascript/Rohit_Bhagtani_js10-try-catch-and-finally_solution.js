

/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    try{
        if(typeof(s) == "number")throw s;}
    catch(err){
        console.log("s.split is not a function");
        console.log(s );
    }
    finally{
        if(typeof(s) == "string"){
        var splitstr = s.split("");
        var revstr = splitstr.reverse();
        var joinstr = revstr.join("");
        console.log(joinstr);
        }
       
    }
}

