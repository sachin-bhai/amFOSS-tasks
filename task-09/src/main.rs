#![allow(non_snake_case)]
extern crate reqwest;

extern crate scraper;



fn main() {

    let response = reqwest::blocking::get(
        "https://www.crypto.com/price",
    )
    .unwrap()
    .text()
    .unwrap();



    let  document = scraper::Html::parse_document(&response);

    let _crypto_selector = scraper::Selector::parse("tr.css-1cxc880").unwrap();
    let _crypto_name_selector = scraper::Selector::parse("span.chakra-text.css-1jj7b1a").unwrap();
    let _crypto_price_selector = scraper::Selector::parse("div.css-b1ilzc").unwrap();
    let _crypto_24hourchange_selector = scraper::Selector::parse("td.css-1b7j986 p").unwrap();
    let _crypto_24hourvolume_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let _crypto_marketcap_selector = scraper::Selector::parse("td.css-1nh9lk8+td").unwrap();

    let mut wtr = csv::Writer::from_path("crypto.csv").unwrap();

    wtr.write_record(&["Crypto Name" , "Price" , "24H Change" , "24H Volume" , "Market cap"]).unwrap();

    for element in document.select(&_crypto_selector) {
        let _crypto_name_element = element.select(&_crypto_name_selector).next().expect("Crypto Name");
        let crypto_name = _crypto_name_element.text().collect::<String>();

        let _crypto_price_element = element.select(&_crypto_price_selector).next().expect("could not select Crypto price");
        let crypto_price = _crypto_price_element.text().collect::<String>();

        let _crypto_24hourchange_element = element.select(&_crypto_24hourchange_selector).next().expect("could not select 24 hour change");
        let crypto_24hourchange = _crypto_24hourchange_element.text().collect::<String>();

        let _crypto_24hourvolume_element = element.select(&_crypto_24hourvolume_selector).next().expect("could not select 24 hour volume");
        let crypto_24hourvolume = _crypto_24hourvolume_element.text().collect::<String>();

        let _crypto_marketcap_element = element.select(&_crypto_marketcap_selector).next().expect("Could not select marketcap");
        let crypto_marketcap = _crypto_marketcap_element.text().collect::<String>();

        wtr.write_record([&crypto_name , &crypto_price , &crypto_24hourchange , &crypto_24hourvolume , &crypto_marketcap]).expect("could not create selector");
    }

    wtr.flush().expect("could not close file");
    println!("done");


}

/*
fn main() {
    let response = reqwest::blocking::get(
        "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&count=100",
    )
    .unwrap()
    .text()
    .unwrap();

    let document = scraper::Html::parse_document(&response);

    let title_selector = scraper::Selector::parse("h3.lister-item-header>a").unwrap();

    let titles = document.select(&title_selector).map(|x| x.inner_html());

    titles
        .zip(1..101)
        .for_each(|(item, number)| println!("{}. {}", number, item));
}*/
