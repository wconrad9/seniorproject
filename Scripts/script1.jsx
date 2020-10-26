#script addMav
#target aftereffects

//var firstComp = app.project.item(1);
//alert("number of layers is " + firstComp.numLayers);
//alert("name of last layer is " + firstComp.layer(firstComp.numLayers).name);

var clip = app.project.importFileWithDialog();

//(name, width, height, ,duration, fr)
var newComp = app.project.items.addComp("Lapse1", 1920, 1080, 1, 20, 120.00);

//FILE (["./test.mp4"]);

//var myFolder = Folder.selectDialog("Choose a folder");
//var allFiles = myFolder.getFiles();
var layer1 = newComp.layers.add(app.project.item(1), 20);


//FILE.openDialog("choose file", multiselect = false);

var bf101path = "/Volumes/Workspaces/wc/SeniorWork/BeldenFalls.10.1";

//print(bf101path);




