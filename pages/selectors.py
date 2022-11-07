"""Локаторы для главной страницы"""
user_header_button_selector: str = 'a[data-statlog="headline.avatar"]'
enter_button_selector: str = 'a[data-statlog="headline.enter"]'
user_menu_links_selector: str = 'div.usermenu-redesign__list>a'

"""Локаторы для страницы авторизации"""
login_input_selector: str = 'input#passp-field-login'
mail_login_selector: str = 'button[data-type="login"]'
password_input_selector: str = 'input#passp-field-passwd'

"""Локаторы для страницы Диска"""
create_button_selector: str = 'span.create-resource-popup-with-anchor'
creatable_items_selector: str = 'button.create-resource-button'
create_item_input_selector: str = 'input[value="Новая папка"]'
listing_items_selector: str = 'div.listing-item__info > div.listing-item__title'
context_menu_selector: str = 'div[role="menuitem"]'
modal_elements_selector: str = 'div.b-tree__name'
confirm_modal_button_selector: str = 'button.confirmation-dialog__button_submit'
disk_root_page_selector: str = 'div.crumbs2__head'
user_header_button_in_disk_selector: str = 'div.PSHeader-User'
user_menu_links_in_disk_selector: str = 'ul.menu > ul > li, div.legouser__multi-auth, div.legouser__menu-footer > a'
