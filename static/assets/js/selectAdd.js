var select = $("#scripSel");
var IDs = 0

for (let item in allQuotes){
    var opt = document.createElement('option');
    opt.value = IDs;
    IDs++;
    opt.text = item + " -- " + allQuotes[item]
    select.append(opt);
}