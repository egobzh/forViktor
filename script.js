document.addEventListener('DOMContentLoaded', () => {

    // Элементы модального окна
    const modal = document.getElementById('modal');
    const modalBody = document.getElementById('modal-body');
    const closeBtn = document.querySelector('.close-btn');

    // Находим все карточки, у которых есть скрытый контент
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('click', () => {
            // 1. Ищем скрытый контент внутри нажатой карточки
            const fullContent = card.querySelector('.full-content');

            // 2. Ищем картинку (или заглушку) в карточке
            const imgPlaceholder = card.querySelector('.card-img-placeholder');
            const imgReal = card.querySelector('img');

            if (fullContent) {
                // Очищаем старое содержимое модалки
                modalBody.innerHTML = '';

                // Если есть картинка, клонируем её в модалку
                if (imgReal) {
                    const imgClone = imgReal.cloneNode(true);
                    modalBody.appendChild(imgClone);
                } else if (imgPlaceholder) {
                    // Если картинки нет, можно ничего не добавлять или добавить заглушку
                }

                // Добавляем текст
                modalBody.innerHTML += fullContent.innerHTML;

                // Открываем окно
                modal.classList.add('active');
            }
        });
    });

    // Закрытие модального окна по крестику
    closeBtn.addEventListener('click', () => {
        modal.classList.remove('active');
    });

    // Закрытие по клику вне белого окна
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
        }
    });
});