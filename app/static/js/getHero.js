function select(index) {

    const id = document.getElementById(index).getAttribute("data-id")
    const name = document.getElementsByClassName("name")[index].innerHTML;
    const description = document.getElementsByClassName("description")[index].innerHTML
    const image = document.getElementsByClassName("image")[index].src

    const dict_values = {description, image, name, id} //Pass the javascript variables to a dictionary.
    const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string

    $.ajax({
        url:"/chosen",
        type:"POST",
        contentType: "application/json",
        data: s
    });

}