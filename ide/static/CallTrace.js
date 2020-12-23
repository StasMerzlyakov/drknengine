function CallTraceModule() {

var gStack = []
var gLast = null
var LIMIT = 40

// Autogenerated with DRAKON Editor 1.32


function add(name, args) {
    // item 33
    var trace = [name]
    // item 34
    if (args) {
        // item 37
        trace.push(args)
    }
    // item 49
    if (Config.TRACE_TO_CONSOLE) {
        // item 52
        console.log("CallTrace:add", trace)
    }
    // item 6
    gStack.push(trace)
    // item 60
    if (gStack.length > LIMIT) {
        // item 63
        gStack.shift()
    }
}

function error(ex) {
    // item 48
    add(
    	"Exception",
    	[ex.name, ex.message, ex.fileName, ex.stack]
    )
}

function getNames() {
    // item 42
    return gStack.map(function(trace) {
    	return trace[0]
    })
}

function peek() {
    // item 32
    return gLast
}

function reset() {
    // item 64
    return gStack
}


this.add = add
this.reset = reset
this.peek = peek
this.getNames = getNames
this.error = error

}

var CallTrace = new CallTraceModule()