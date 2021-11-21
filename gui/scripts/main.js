function openTab(evnt, tabName, clicked) {
    if(!(clicked.className === "tablinks inactive")){
        var i, tabcontent, tablinks;

        tabcontent = document.getElementsByClassName("tabcontent");
        for(i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }

        tablinks = document.getElementsByClassName("tablinks");
        for(i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "")
        }

        document.getElementById(tabName).style.display = "block";
        evnt.currentTarget.className += " active";
    }
}