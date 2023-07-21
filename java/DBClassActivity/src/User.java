public class User {
    private String first_name;
    private String last_name;
    private Integer phone_number;
    private String sex;
    private String date_of_birth;
    private String street;
    private String city;
    private String state;
    private String country;
    private Integer zip_code;
    private String name;
    private String profession;
    private Integer address_id;
    private Integer contact_id;
    private Integer referee_id;

    // constructor for address
    public User(String street, String city, String state, String country, Integer zip_code){
        this.street = street;
        this.city = city;
        this.state = state;
        this.country = country;
        this.zip_code = zip_code;
    }

    // constructor for referee
    public User(String name, Integer phone_number, String profession, Integer address_id){
        this.name = name;
        this.phone_number = phone_number;
        this.profession = profession;
        this.address_id = address_id;
    }

    // constructor for contact
    public User(String first_name, String last_name, Integer phone_number, String sex, String date_of_birth){
        this.first_name = first_name;
        this.last_name = last_name;
        this.phone_number = phone_number;
        this.sex = sex;
        this.date_of_birth = date_of_birth;
    }

    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public Integer getPhone_number() {
        return phone_number;
    }

    public void setPhone_number(Integer phone_number) {
        this.phone_number = phone_number;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getDate_of_birth() {
        return date_of_birth;
    }

    public void setDate_of_birth(String date_of_birth) {
        this.date_of_birth = date_of_birth;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public Integer getZip_code() {
        return zip_code;
    }

    public void setZip_code(Integer zip_code) {
        this.zip_code = zip_code;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getProfession() {
        return profession;
    }

    public void setProfession(String profession) {
        this.profession = profession;
    }

    public Integer getAddress_id() {
        return address_id;
    }

    public void setAddress_id(Integer address_id) {
        this.address_id = address_id;
    }

    public Integer getContact_id() {
        return contact_id;
    }

    public void setContact_id(Integer contact_id) {
        this.contact_id = contact_id;
    }

    public Integer getReferee_id() {
        return referee_id;
    }

    public void setReferee_id(Integer referee_id) {
        this.referee_id = referee_id;
    }
}
