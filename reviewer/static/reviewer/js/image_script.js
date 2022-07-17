// https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types
const fileTypes = [
  "image/apng",
  "image/bmp",
  "image/gif",
  "image/jpeg",
  "image/pjpeg",
  "image/png",
  "image/svg+xml",
  "image/tiff",
  "image/webp",
  "image/x-icon"
];
//
// image input
const image_input = document.querySelector('input[type="file"]');
const image_preview = document.querySelector('.preview');
const post_review = document.querySelector(".new-review-button")

// hide file input
image_input.style.opacity = 0;


// add event listener
image_input.addEventListener('change', updateImageDisplay);

// function to preview uploades images
function updateImageDisplay() {
  while(image_preview.firstChild) {
    image_preview.removeChild(image_preview.firstChild);
  }

  const curFiles = image_input.files;
  if(curFiles.length === 0) {
    const para = document.createElement('p');
    para.textContent = 'No files currently selected for upload';
    // image_preview.appendChild(para);
  } else {
    if(curFiles.length > 4) {
      alert("Maximum number of files exceeded! Upload a maximum of 4 images");
    } else {

      const list = document.createElement('ol');
      image_preview.appendChild(list);
  
      for(const file of curFiles) {
        const listItem = document.createElement('li');
        const imageBox = document.createElement('div');
        const para = document.createElement('p');
        if(validFileType(file)) {
          para.textContent = `file size ${returnFileSize(file.size)}.`;
          const image = document.createElement('img');
          image.src = URL.createObjectURL(file);
  
          imageBox.className = "image-preview-box";
          imageBox.appendChild(image);
          // imageBox.appendChild(para);
          listItem.appendChild(imageBox);
        } else {
          para.textContent = `File name ${file.name}: Not a valid file type. Update your selection.`;
          // listItem.appendChild(para);
        }
  
        list.appendChild(listItem);
      }
    }
  }
}

// function to validate file types
function validFileType(file) {
  return fileTypes.includes(file.type);
}

// function to return the file size
function returnFileSize(number) {
  if(number < 1024) {
    return number + 'bytes';
  } else if(number >= 1024 && number < 1048576) {
    return (number/1024).toFixed(1) + 'KB';
  } else if(number >= 1048576) {
    return (number/1048576).toFixed(1) + 'MB';
  }
}
