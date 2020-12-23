#script addMav
#target aftereffects


app.beginUndoGroup("Automagic");
//var firstComp = app.project.item(1);
//alert("number of layers is " + firstComp.numLayers);
//alert("name of last layer is " + firstComp.layer(firstComp.numLayers).name);

var myFolder = new Folder(app.project.importFileWithDialog());
var myImportOptions = new ImportOptions();
var importedLayers = new Array();

var myVids = myFolder.getFiles("*.mp4");
var myAud = myFolder.getFiles("*.wav");
var allMedia = myVids.concat(myAud);

var numFiles = allMedia.length;

var numAudio = 0;
var numVisual = 0;

var audioArray = new Array();
var videoArray = new Array();

for(var i = 0; i<allMedia.length;i++){
    myImportOptions.file = allMyFiles[i];
    importedLayers.push(app.project.importFile(myImportOptions));

}

var duration = 0;
for(var e = 1; e <= app.project.numItems;e++){

    if(app.project.item(e).hasVideo==true){
        numVisual++;
        videoArray.push(app.project.item(e));
        duration += app.project.item(e).duration;
    }
    if(app.project.item(e).hasVideo==false && app.project.item(e).hasAudio==true){
        numAudio++;
        audioArray.push(app.project.item(e));
    }
}

var tempComp = app.project.items.addComp("test", 1920,1080,1,duration, 2);
tempComp.openInViewer();

var startTime = 0;
for(var q = 0; q < videoArray.length;q++){
    var thisLayer = tempComp.layers.add(videoArray[q]);
    thisLayer.audioEnabled = false;
    thisLayer.startTime=startTime;
    var opac = thisLayer.opacity;
    opac.setValueAtTime(thisLayer.startTime, 0);
    opac.setValueAtTime(thisLayer.startTime + numVisual*10, 100);
    startTime = thisLayer.startTime + 10;
}

var startTime = 0;
var audioLayer = tempComp.layers.add(audioArray[0]);
for(var z = 0; q < audioArray.length;z++){
    var thisLayer = tempComp.layers.add(audioArray[z]);
    thisLayer.startTime = startTime;
    //startTime = thisLayer.outPoint;
}
audioLayer.outPoint = duration;

var myFile = new File("~/Desktop" + tempComp.name + ".mov"); 

alert('pause');

//var lapse1 = app.project.importFileWithDialog();
//var lapse2 = app.project.importFileWithDialog();
//var lapses = Folder.selectDialog("choose lapses");

//(name, width, height, ,duration, fr)

//var layer1 = newComp.layers.add(app.project.item(1), 20);
var opac1 = layer1.opacity;
opac1.setValueAtTime(0,0);
opac1.setValueAtTime(20,100);

//var layer2 = newComp.layers.add(app.project.item(2), 20);
var opac2 = layer2.opacity;
opac2.setValueAtTime(0,100);
opac2.setValueAtTime(20,0);

app.endUndoGroup(); 
//FILE (["./test.mp4"]);

//var myFolder = Folder.selectDialog("Choose a folder");
//var allFiles = myFolder.getFiles();
//var layer1 = newComp.layers.add(app.project.item(2), 20);


//FILE.openDialog("choose file", multiselect = false);

//print(bf101path);




