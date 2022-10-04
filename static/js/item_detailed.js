const addToFavourite = async ({ item }) => {
  const favouriteButton = document.getElementById(`${item}-favourite`)
  try {
    const response = await fetch(`/favorite-item/${item}`, { method: "GET" })
    const data = await response.json()
    console.log(data)
    if (response.status == 400) {
      alert(data)
      return
    }
    favouriteButton.className = data.fav_class
  } catch (error) {
    console.error(error)
  }
}

const addToWishList = async ({ item }) => {
  console.log(item)
}
