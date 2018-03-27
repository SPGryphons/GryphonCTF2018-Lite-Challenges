function checkFlag() {
    var x = document.getElementById("flag");
    if (x.value === "GCTF{n0t_s0_s1mple_0bfusc4t10n}") {
        alert("Correct!");
    } else {
        alert("Wrong!");
    }
}
window.onload = function() {
    document.getElementById("btn").onclick = function fun() {
        checkFlag();
        location.reload();
    }
}