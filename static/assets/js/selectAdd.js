

console.log(allQuotes["ATGL"]);

// stockCodes = (json);
var select = $("#scripSel");
var ids = 0

for (let item in allQuotes){
    var opt = document.createElement('option');
    opt.value = ids;
    ids++;
    opt.text = item + " -- " + allQuotes[item]
    select.append(opt);
}