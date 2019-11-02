// If a token ends in :, it needs quotes. If a token is wrapped in '', it needs quotes.

/*
 * Repairs a malformed json string missing double-quotes.
 */
function jsonifyBadJson(badJson) {
    let savedIndex;

    // Convert all the single-quotes ('') to double-quotes ("").
    for (let strPtr = 0; strPtr < badJson.length; strPtr++) {
        if (badJson.charAt(strPtr) === '\'') {
            badJson = setCharAt(badJson, strPtr, '\"');
        }
    }

    // Once you see a colon, add a quote before. Then go back,
    // and once you see a char that isn't alphabetical or an
    // underscore, add a quote after it.
    for (let strPtr = 0; strPtr < badJson.length; strPtr++) {
        if (badJson.charAt(strPtr) === ':') {
            savedIndex = strPtr;
            badJson = insertCharAtPriorIndex(badJson, strPtr, '\"');
            strPtr--; // Should be before new quote mark.

            // Loop to char before token.
            while (badJson.charAt(strPtr) === '_' || isLetter(badJson.charAt(strPtr))) {
                strPtr--;
            }

            // Add quote mark in front of current char.
            badJson = insertCharAtPriorIndex(badJson, strPtr + 1, '\"');

            // Increment strPtr to char after : of modified token.
            strPtr = savedIndex + 2;
        }
    }

    // Make ID value a string.
    for (let strPtr = 0; strPtr < badJson.length; strPtr++) {
        if (badJson.charAt(strPtr) === 'i' && badJson.charAt(strPtr+1) === 'd' && badJson.charAt(strPtr+2) === '\"') {
            // Jump to start of id and prepend quote mark
            strPtr += 5;
            badJson = insertCharAtPriorIndex(badJson, strPtr, '\"');

            // Inster quote mark at end of id
            while (badJson.charAt(strPtr) !== ',') {
                strPtr++;
            }
            badJson = insertCharAtPriorIndex(badJson, strPtr, '\"');
        }
    }

    return badJson;
}

function setCharAt(str,index,chr) {
    if(index > str.length-1) return str;
    return str.substr(0,index) + chr + str.substr(index+1);
}

function insertCharAtPriorIndex(str, index, char) {
    return [str.slice(0, index), char, str.slice(index)].join('');
}

function isLetter(char) {
    return char.length === 1 && char.match(/[A-Z0-9]/i);
}

module.exports.jsonifyBadJson = jsonifyBadJson;


/*
var a = "I want apple";
var b = "an";
var position = 6;
var output = [a.slice(0, position), b, a.slice(position)].join('');

I wantan apple

*/
