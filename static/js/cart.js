const updateItemPlus = ({ item }) => {
  const itemCountField = document.getElementById(`${item}-item-counter`);
  const itemCountFieldActual = document.getElementById(
    `${item}-item-counter-value`
  );
  const itemTotalPrice = document.getElementById(`${item}-total-price`);
  const itemActualPrice = document.getElementById(`${item}-actual-price`);

  const count = parseInt(itemCountField.value);
  if (itemCountField.value < 10) {
    itemCountField.value = count + 1;
    itemTotalPrice.innerText = itemCountField.value * itemActualPrice.innerText;
    itemCountFieldActual.value = itemCountField.value;
  }
};

const updateItemMinus = ({ item }) => {
  const itemCountField = document.getElementById(`${item}-item-counter`);
  const itemTotalPrice = document.getElementById(`${item}-total-price`);
  const itemActualPrice = document.getElementById(`${item}-actual-price`);
  const itemCountFieldActual = document.getElementById(
    `${item}-item-counter-value`
  );

  const count = parseInt(itemCountField.value);
  if (itemCountField.value > 1) {
    itemCountField.value = count - 1;
    itemTotalPrice.innerText = itemCountField.value * itemActualPrice.innerText;
    itemCountFieldActual.value = itemCountField.value;
  }
};
