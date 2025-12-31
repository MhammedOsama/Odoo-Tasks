# Custom Sale Extension Module

## Installation

1. Copy the module to your Odoo custom_addons directory:
   ```
   /path/to/odoo/custom_addons/custom_sale_extension
   ```

2. Update Apps List in Odoo:
   - Go to Apps menu
   - Click "Update Apps List"

3. Install the module:
   - Search for "Custom Sale Extension"
   - Click "Install"

4. Restart Odoo server (if needed):
   ```bash
   ./odoo-bin -c odoo.conf -u custom_sale_extension
   ```

## Testing Steps

### Test 1: Delivery Note Field
1. Go to Sales → Orders → New
2. Fill required fields and save
3. Check the "Extra Info" tab - delivery note should be auto-generated

### Test 2: Delivery Note in PDF
1. Open any Sales Order
2. Click Print → Quotation / Order
3. Check PDF - delivery note should appear below order lines

### Test 3: API Endpoint
1. Make sure you are logged into Odoo
2. Access: `GET http://localhost:8069/api/sale_orders/latest`
3. Should return JSON with last 10 sales orders

### Test 4: Return Policy Settings
1. Go to Settings → Invoicing
2. Find "Return Policy" section
3. Set "Number of Days for Invoice Return" (default: 30)
4. Click Save

### Test 5: Credit Note Validation
1. Set return days to 10 in Settings
2. Find an invoice older than 10 days
3. Try to create a credit note for it
4. Should show error: "Cannot save credit note. The invoice date is X days ago, which exceeds the allowed 10 days."

### Test 6: Valid Credit Note
1. Create a credit note for an invoice less than 10 days old
2. Should save successfully without errors
