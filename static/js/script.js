function textCopier(event) {
    event.preventDefault()
    let copyText = document.getElementById("copyurl").src;
    let textArea = document.createElement("textarea");
    textArea.value = copyText;
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    textArea.setSelectionRange(0, 99999); /* For mobile devices */
    document.execCommand("copy");
    window.alert('You have copied image location '  + textArea.value);
    document.body.removeChild(textArea);
}