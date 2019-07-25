let button= document.querySelector("#like-button");
let like_header= document.querySelector("#My-Likes")
let like_count = 0;
button.addEventListener("click", () =>{
  like_count++;
  like_header.innerHTML ="you have " + like_count + "likes.")
});
