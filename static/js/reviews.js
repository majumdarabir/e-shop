const likeReview = async ({ review }) => {
  const likeCountElement = document.getElementById(`${review}-like-count`)
  const likeButtonElement = document.getElementById(`${review}-like-button`)

  try {
    const request = await fetch(`/like-review/${review}`, { method: "GET" })
    const data = await request.json()
    if (request.status == 400) {
      alert(await data.detail)
      return
    }
    console.log(data)
  } catch (error) {
    console.error(error)
  }

  // const likeCount = parseInt(likeCountElement.innerText)
  // likeButton.className = "fa-solid fa-thumbs-up"
}
const unlikeReview = async ({ review }) => {
  const unlikeCountElement = document.getElementById(`${review}-unlike-count`)
  const unlikeButtonElement = document.getElementById(`${review}-unlike-button`)
  try {
    const request = await fetch(`/unlike-review/${review}`, { method: "GET" })
    const data = await request.json()
    if (request.status == 400) {
      alert(await data.detail)
      return
    }
    unlikeButtonElement.className = "fa-solid fa-thumbs-up"
    unlikeCountElement.innerText = data.un_like_count
  } catch (error) {
    console.error(error)
  }
}
