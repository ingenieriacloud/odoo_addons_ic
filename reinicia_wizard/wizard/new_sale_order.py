# -*- encoding: utf-8 -*-
from openerp.osv import orm, fields


class NewSaleOrderWizard(orm.TransientModel):
    _name = 'sale.order.new_wizard'
    _description = "Creates a new sale order"

    _columns = {
        'customer': fields.many2one('res.partner', 'Cliente'),
        'prods' : fields.many2many('stock.quant', 'product_id')
    }

    def _get_active_ids(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        #dom = [('id','in',context.get("active_ids", []))]
        #quants = self.pool.get('stock.quant').search(cr, uid, dom, context=context)
        #return quants or False
        return context.get("active_ids", False)

    _defaults = {
        'prods' : _get_active_ids,
        }
    
    def action_new(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        data = self.browse(cr, uid, ids[0], context=context)
        sale_order_obj = self.pool['sale.order']
        ctx = context.copy()

        vals = {}
        
        vals['partner_id'] = data.customer.id
        
        id_sale = sale_order_obj.create(cr, uid,
                                        vals,
                                        context=ctx)
        vals['order_id'] = id_sale

        sale_order_line_obj = self.pool['sale.order.line']
        dom = [('id','in',context.get("active_ids", []))]
        quants = self.pool.get('stock.quant').search(cr, uid, dom, context=context)
        for quant in self.pool.get('stock.quant').browse(cr, uid, quants, context=context):
            vals['product_id'] = quant.product_id.id
            vals['product_uom_qty'] = quant.qty
            vals['quant_id'] = quant.id
            vals['lot_id'] = quant.lot_id.id
            vals['name'] = quant.product_id.description_sale or quant.product_id.name
            sale_order_line = sale_order_line_obj.create(cr, uid,
                                                         vals,
                                                         context=ctx)
        

        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order',
            'res_model': 'sale.order',
            'res_id': id_sale ,
            'view_type': 'form',
            'view_mode': 'form',
            #'target' : 'new',
        }
