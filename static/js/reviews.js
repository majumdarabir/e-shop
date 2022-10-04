const likeReview = async ({ review }) => {
  const likeCountElement = document.getElementById(`${review}-like-count`)
  const likeButtonElement = document.getElementById(`${review}-like-button`)
  const unlikeCountElement = document.getElementById(`${review}-unlike-count`)
  const unlikeButtonElement = document.getElementById(`${review}-unlike-button`)

  try {
    const request = await fetch(`/like-review/${review}`, { method: "GET" })
    const data = await request.json()
    console.log(data)
    if (request.status == 400) {
      alert(await data.detail)
      return
    }
    likeButtonElement.className = data.like_class
    if (data.unlike_class !== undefined) {
      unlikeButtonElement.className = data.unlike_class
    }
    unlikeCountElement.innerText = data.un_like_count
    likeCountElement.innerText = data.like_count
  } catch (error) {
    console.error(error)
  }
}
const unlikeReview = async ({ review }) => {
  const likeCountElement = document.getElementById(`${review}-like-count`)
  const likeButtonElement = document.getElementById(`${review}-like-button`)
  const unlikeCountElement = document.getElementById(`${review}-unlike-count`)
  const unlikeButtonElement = document.getElementById(`${review}-unlike-button`)
  try {
    const request = await fetch(`/unlike-review/${review}`, { method: "GET" })
    const data = await request.json()
    console.log(data)
    if (request.status == 400) {
      alert(await data.detail)
      return
    }
    unlikeButtonElement.className = data.unlike_class
    if (data.like_class != undefined) {
      likeButtonElement.className = data.like_class
    }
    unlikeCountElement.innerText = data.un_like_count
    likeCountElement.innerText = data.like_count
  } catch (error) {
    console.error(error)
  }
}
