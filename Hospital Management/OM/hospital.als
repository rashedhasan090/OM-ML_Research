module hospital
open Declaration

one sig Permission extends Class{}{
attrSet = permissionID+permission_role_ID+permission_Title+permission_Module+permission_Description
id=permissionID
isAbstract = No
no parent
}

one sig permissionID extends Integer{}
one sig permission_role_ID extends string{}
one sig permission_Title extends string{}
one sig permission_Module extends string{}
one sig permission_Description extends string{}



one sig User extends Class{}{
attrSet = userID+user_role_ID+user_name+user_email+user_dob+user_address
one parent
id=permissionID
isAbstract = No
parent in Permission
}

one sig userID extends Integer{}
one sig user_role_ID extends string{}
one sig user_name extends string{}
one sig user_email extends string{}
one sig user_dob extends string{}
one sig user_address extends string{}

one sig Role extends Class{}{
attrSet = roleID+roleTitle+roleDescription
id=roleID
isAbstract = No
no parent
}

one sig roleID extends Integer{}
one sig roleTitle extends string{}
one sig roleDescription extends string{}

one sig Booking extends Class{}{
attrSet = bookingID+booking_type+booking_title+booking_description+booking_date
id=bookingID
isAbstract = No
no parent
}

one sig bookingID extends Integer{}
one sig booking_type extends string{}
one sig booking_title extends string{}
one sig booking_description extends string{}
one sig booking_date extends string{}



one sig PermissionBookingAssociation extends Association{}{
src = Permission
dst = Booking
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig Customer extends Class{}{
attrSet = customerID+customer_name+customer_mobile+customer_email+customer_address+customer_username+customer_password
id=customerID
isAbstract = No
no parent
}

one sig customerID extends Integer{}
one sig customer_name extends string{}
one sig customer_mobile extends string{}
one sig customer_email extends string{}
one sig customer_address extends string{}
one sig customer_username extends string{}
one sig customer_password extends string{}


one sig CustomerPermissonAssociation extends Association{}{
src = Customer
dst = Permission
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig Rooms extends Class{}{
attrSet = roomID+room_exam_ID+room_number+room_type+room_description
id=roomID
isAbstract = No
no parent
}

one sig roomID extends Integer{}
one sig room_exam_ID extends string{}
one sig room_number extends string{}
one sig room_type extends string{}
one sig room_description extends string{}

one sig RoomsPermissonAssociation extends Association{}{
src = Rooms
dst = Permission
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig Hotel extends Class{}{
attrSet = hotelID+hotel_description+hotel_type+hotel_name+hotel_rent+hotel_address
id=hotelID
isAbstract = No
no parent
}

one sig hotelID extends Integer{}
one sig hotel_description extends string{}
one sig hotel_type extends string{}
one sig hotel_name extends string{}
one sig hotel_rent extends string{}
one sig hotel_address extends string{}


one sig HotelPermissonAssociation extends Association{}{
src = Hotel
dst = Permission
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig Payment extends Class{}{
attrSet = paymentID+payment_customer_ID+payment_description+payment_date
id=ItemID
isAbstract = No
no parent
}

one sig paymentID extends Integer{}
one sig payment_customer_ID extends string{}
one sig payment_description extends string{}
one sig payment_date extends string{}

one sig PaymentPermissonAssociation extends Association{}{
src = Payment
dst = Permisson
src_multiplicity = MANY
dst_multiplicity = MANY
}

pred show{}
run show for 48
