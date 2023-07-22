import java.util.*;
import java.io.*;
import java.sql.*;

public class PopulateDB {
    public static void populateDB() throws IOException, ClassNotFoundException, Exception {
        while (true) {
            System.out.printf("Enter %d to insert a record.\n", 1);
            System.out.printf("Enter %d to exit.\n", 0);

            Scanner userChoice = new Scanner(System.in);
            System.out.print("Enter your choice: ");
            int choice = userChoice.nextInt();

            if (choice == 1) {
                try(Connection connection = DriverManager.getConnection(Main.DB_URL)){

                    // get the contact information
                    User contact = new User();
                    System.out.println("Bayron Connection Successful!");
                    Scanner userFirstName = new Scanner(System.in);
                    System.out.print("Enter contact first name: ");
                    String firstName = userFirstName.nextLine();
                    Scanner userLastName = new Scanner(System.in);
                    System.out.print("Enter contact last name: ");
                    String lastName = userLastName.nextLine();
                    Scanner userPhoneNumber = new Scanner(System.in);
                    System.out.print("Enter contact phone number (last 5 digits): ");
                    Integer phoneNumber = Integer.valueOf(userPhoneNumber.nextLine());
                    Scanner userSex = new Scanner(System.in);
                    System.out.print("Enter contact sex (Male/Female): ");
                    String sex = userSex.nextLine();
                    Scanner userDateOfBirth = new Scanner(System.in);
                    System.out.print("Enter contact date of birth (YYYY-MM-DD) without the dashes: ");
                    String dateOfBirth = userDateOfBirth.next();
                    contact.setFirst_name(firstName);
                    contact.setLast_name(lastName);
                    contact.setPhone_number(phoneNumber);
                    contact.setSex(sex);
                    contact.setDate_of_birth(dateOfBirth);
                    String result = Contact.createContact(contact);
                    System.out.println(result);

                    // get the address information of the contact
                    User contactAddressDetails = new User();
                    Scanner contactStreet = new Scanner(System.in);
                    System.out.print("Enter contact street: ");
                    String contactStreetName = contactStreet.nextLine();
                    Scanner contactCity = new Scanner(System.in);
                    System.out.print("Enter contact city: ");
                    String contactCityName = contactCity.nextLine();
                    Scanner contactState = new Scanner(System.in);
                    System.out.print("Enter contact state: ");
                    String contactStateName = contactState.nextLine();
                    Scanner contactCountry = new Scanner(System.in);
                    System.out.print("Enter contact country: ");
                    String contactCountryName = contactCountry.nextLine();
                    Scanner contactZipCode = new Scanner(System.in);
                    System.out.print("Enter contact zip code (5-6 digits): ");
                    Integer contactZipCodeNumber = contactZipCode.nextInt();
                    contactAddressDetails.setStreet(contactStreetName);
                    contactAddressDetails.setCity(contactCityName);
                    contactAddressDetails.setState(contactStateName);
                    contactAddressDetails.setCountry(contactCountryName);
                    contactAddressDetails.setZip_code(contactZipCodeNumber);
                    String resultAddress = Address.createAddress(contactAddressDetails);
                    System.out.println(resultAddress);

                    // get the contact ID and address ID and update the contactAddress table
                    User contact_id = Contact.selectContactID();
                    User contact_address_id = Address.selectAddressID();
                    if (contact_address_id != null && contact_id != null) {
                        ContactAddress.createContactAddressLink(contact_address_id, contact_id);
                    }

                    // get the address information of the referee
                    User refereeAddressDetails = new User();
                    Scanner refereeStreet = new Scanner(System.in);
                    System.out.print("Enter referee street: ");
                    String refereeStreetName = refereeStreet.nextLine();
                    Scanner refereeCity = new Scanner(System.in);
                    System.out.print("Enter referee city: ");
                    String refereeCityName = refereeCity.nextLine();
                    Scanner refereeState = new Scanner(System.in);
                    System.out.print("Enter referee state: ");
                    String refereeStateName = refereeState.nextLine();
                    Scanner refereeCountry = new Scanner(System.in);
                    System.out.print("Enter referee country: ");
                    String refereeCountryName = refereeCountry.nextLine();
                    Scanner refereeZipCode = new Scanner(System.in);
                    System.out.print("Enter referee zip code (5-6 digits): ");
                    Integer refereeZipCodeNumber = Integer.valueOf(contactZipCode.nextLine());
                    refereeAddressDetails.setStreet(refereeStreetName);
                    refereeAddressDetails.setCity(refereeCityName);
                    refereeAddressDetails.setState(refereeStateName);
                    refereeAddressDetails.setCountry(refereeCountryName);
                    refereeAddressDetails.setZip_code(refereeZipCodeNumber);
                    String refereeAddress = Address.createAddress(refereeAddressDetails);
                    System.out.println(refereeAddress);

                    // get the referee details
                    User referee = new User();
                    Scanner refereeName = new Scanner(System.in);
                    System.out.print("Enter referee name: ");
                    String refereeNameName = refereeName.nextLine();
                    Scanner refereePhoneNumber = new Scanner(System.in);
                    System.out.print("Enter referee phone number (last 5 digits): ");
                    Integer refereePhoneNumberNumber = Integer.valueOf(refereePhoneNumber.nextLine());
                    Scanner refereeProfession = new Scanner(System.in);
                    System.out.print("Enter referee profession: ");
                    String refereeProfessionName = refereeProfession.nextLine();
                    referee.setName(refereeNameName);
                    referee.setPhone_number(refereePhoneNumberNumber);
                    referee.setProfession(refereeProfessionName);
                    // get the integer value of the address ID
                    User a_ID = Address.selectAddressID();
                    if (a_ID != null) {
                        referee.setAddress_id(a_ID.getAddress_id());
                    }
                    String refereeDetails = Referee.createReferee(referee);
                    System.out.println(refereeDetails);

                    // get contact_id and referee_id and update the contactReferee table
                    User contact_ID = Contact.selectContactID();
                    User contact_referee_id = Referee.selectRefereeID();
                    if (contact_ID != null && contact_referee_id != null) {
                        ContactReferees.createContactRefereeLink(contact_ID, contact_referee_id);
                    }

                }catch(SQLException omoENoWorkO) {
                    omoENoWorkO.printStackTrace();
                }
            } else if (choice == 0) {
                System.out.println("Hope to see you next time!!!");
                System.exit(0);
            }
            else {
                System.out.println("Invalid input. Please try again.");
                break;
            }
        }
    }
}
