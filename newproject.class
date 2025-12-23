function getAbsoluteXPath(element) {
    if (element === document.body)
        return '/html/body';
    var comp, comps = [];
    var parent = null;
    var xpath = '';
    var getPos = function(element) {
        var siblings = element.parentNode ? element.parentNode.children : [];
        var count = 0;
        var index = -1;
        for (var i = 0; i < siblings.length; i++) {
            var sib = siblings[i];
            if (sib.nodeName === element.nodeName) {
                count++;
                if (sib === element) {
                    index = count;
                }
            }
        }
        return count > 1 ? index : null;
    };

    for (; element && element.nodeType === 1; element = element.parentNode) {
        comp = {};
        comp.name = element.nodeName.toLowerCase();
        var pos = getPos(element);
        if (pos !== null) {
            comp.name += '[' + pos + ']';
        }
        comps.push(comp);
    }

    for (var i = comps.length - 1; i >= 0; i--) {
        xpath += '/' + comps[i].name;
    }
    return xpath;
}

// Example usage: right-click on any element, run this in the console
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    var xpath = getAbsoluteXPath(e.target);
    alert('Absolute XPath: ' + xpath);
}, false);