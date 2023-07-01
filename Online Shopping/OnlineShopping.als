module OnlineShopping
open Declaration

// Web User class
one sig WebUser extends Class{}{
  attrSet = login_id + Password
  id = login_id
  isAbstract = No
  no parent
}

one sig login_id extends String{}
one sig Password extends String{}

// Customer class
one sig Customer extends Class{}{
  attrSet = customer_id + Address + Phone + Email
  id = customer_id
  isAbstract = No
  no parent
}

one sig customer_id extends Integer{}
one sig Address extends String{}
one sig Phone extends String{}
one sig Email extends String{}

// Web User to Customer association
one sig WebUserCustomerAssociation extends Association{}{
  src = WebUser
  dst = Customer
  src_multiplicity = ONE
  dst_multiplicity = ONE
}

// Customer to Web User association
one sig CustomerWebUserAssociation extends Association{}{
  src = Customer
  dst = WebUser
  src_multiplicity = ONE
  dst_multiplicity = ONE
}

// Account class
one sig Account extends Class{}{
  attrSet = Accountid + billing_address + Status + OpeningDate + ClosingDate
  id = Accountid
  isAbstract = No
  no parent
}

one sig Accountid extends Integer{}
one sig billing_address extends String{}
one sig Status extends String{}
one sig OpeningDate extends String{}
one sig ClosingDate extends String{}

// Account to Customer association
one sig AccountCustomerAssociation extends Association{}{
  src = Account
  dst = Customer
  src_multiplicity = ONE
  dst_multiplicity = ONE
}

// Payment class
one sig Payment extends Class{}{
  attrSet = Paymentid + Payment_date + Total + Details
  id = Paymentid
  isAbstract = No
  no parent
}

one sig Payment_id extends Integer{}
one sig Payment_date extends String{}
one sig Total extends Integer{}
one sig Details extends String{}

// Account to Payment association
one sig AccountPaymentAssociation extends Association{}{
  src = Account
  dst = Payment
  src_multiplicity = ONE
  dst_multiplicity = MANY
}

// Payment to Account association
one sig PaymentAccountAssociation extends Association{}{
  src = Payment
  dst = Account
  src_multiplicity = ZERO_MANY
  dst_multiplicity = MANY
}

// Order class
one sig Order extends Class{}{
  attrSet = OrderId + OrderDate + ShippingDate + ShippingAddress + OrderStatus + Total
  id = OrderId
  isAbstract = No
  no parent
}

one sig OrderId extends Integer{}
one sig OrderDate extends String{}
one sig ShippingDate extends String{}
one sig ShippingAddress extends String{}
one sig OrderStatus extends String{}
one sig Total extends Integer{}

// Account to Order association
one sig AccountOrderAssociation extends Association{}{
  src = Account
  dst = Order
  src_multiplicity = ONE
  dst_multiplicity = MANY
}

// Order to Payment association
one sig OrderPaymentAssociation extends Association{}{
  src = Order
  dst = Payment
  src_multiplicity = ONE
  dst_multiplicity = MANY
}

// LineItem class
one sig LineItem extends Class{}{
  attrSet = Quantity + Price
  no parent
  id = none
  isAbstract = No
}

one sig Quantity extends Integer{}
one sig Price extends Integer{}

// Order to Line Item association
one sig OrderLineItemAssociation extends Association{}{
  src = Order
  dst = LineItem
  src_multiplicity = ONE
  dst_multiplicity = MANY
}

one sig Product extends Class{}{
  attrSet = ProductId + ProductName + ProductSupplier
  id = ProductId
  isAbstract = No
  no parent
}

one sig ProductId extends Integer{}
one sig ProductName extends String{}
one sig ProductSupplier extends String{}

// Product to Line Item association
one sig ProductLineItemAssociation extends Association{}{
  src = Product
  dst = LineItem
  src_multiplicity = ONE
  dst_multiplicity = MANY
}

// ShoppingCart class
one sig ShoppingCart extends Class{}{
  attrSet = CreatedDate
  no parent
  id = none
  isAbstract = No
}

one sig CreatedDate extends String{}

// ShoppingCart to Line Item association
one sig ShoppingCartLineItemAssociation extends Association{}{
  src = ShoppingCart
  dst = LineItem
  src_multiplicity = ONE
  dst_multiplicity = MANY
}

// ShoppingCart to Account association
one sig ShoppingCartAccountAssociation extends Association{}{
  src = ShoppingCart
  dst = Account
  src_multiplicity = ONE
  dst_multiplicity = ONE
}

// ShoppingCart to Web User association
one sig ShoppingCartWebUserAssociation extends Association{}{
  src = ShoppingCart
  dst = WebUser
  src_multiplicity = ONE
  dst_multiplicity = ONE
}

pred show {}
run show for 48
